import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO
REGION = "us-east-2"
def detect_labels(photo, bucket):
    client = boto3.client("rekognition",region_name=REGION)
    response = client.detect_labels(
        Image = {"S3Object":{"Bucket":bucket, "Name": photo}},
        MaxLabels = 10
    )
    print("Detected label for "+photo)
    print()
    for label in response["Labels"]:
        print("Label:", label['Name'])
        print("Confidence:", label['Confidence'])
        print()
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket,photo)
    img_data = obj.get()["Body"].read()
    img = Image.open(BytesIO(img_data))

    plt.imshow(img)
    ax = plt.gca()
    for label in response["Labels"]:
        for instance in label.get("Instances", []):
            bbox = instance.get("BoundingBox")
            if not bbox:
                continue

            left = bbox["Left"] * img.width
            top = bbox["Top"] * img.height
            width = bbox["Width"] * img.width
            height = bbox["Height"] * img.height

            rect = patches.Rectangle(
                (left, top), width, height,
                linewidth=2, edgecolor="red", facecolor="none"
            )
            ax.add_patch(rect)

            conf = instance.get("Confidence", label["Confidence"])
            ax.text(
                left, max(top - 5, 0),
                f"{label['Name']} ({conf:.1f}%)",
                fontsize=9,
                bbox=dict(facecolor="white", alpha=0.7)
            )

    plt.axis("off")
    plt.show()
    return len(response['Labels'])

def main():
    bucket = "aws-rekognition-label-images-jerry"
    photo = "cute-puppy-pomeranian-mixed-breed-pekingese-dog-run-on-the-grass-with-happiness-photo.jpg"
    label_count = detect_labels(photo, bucket)
    print("Labels detected:", label_count)


if __name__ == "__main__":
    main()