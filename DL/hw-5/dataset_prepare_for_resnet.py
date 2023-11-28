import glob
import shutil

SOURCE_DIR = r".\dataset_raw"
DESTINATION_DIR = r".\dataset"
PART_SIZES = [0.7, 0.2, 0.1]
TARGET_CLASSES = {
    "fluffy": 0,
    "hairless": 1,
}

print("Starting...")
for cl in TARGET_CLASSES.keys():
    images = [d for d in glob.glob(f"{SOURCE_DIR}\{cl}\*")]

    train, test, val = [int(len(images) * sz) for sz in PART_SIZES]
    test += train
    val += test

    class_ctr = 0

    for i, old_path in enumerate(images):
        if i + 1 <= train:
            mode = "train"
        elif train < i + 1 <= test:
            mode = "test"
        elif i + 1 <= val:
            mode = "val"

        new_path = f"{DESTINATION_DIR}\{mode}\{cl}\{cl}_{class_ctr}.jpg"
        shutil.copy(old_path, new_path)

        class_ctr += 1
print("\nCompleted!")
