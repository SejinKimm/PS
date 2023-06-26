import torch
from torch.utils.data import DataLoader


def ARC_test(num, model):
    model.eval()

    #dataset = ARC eval set
    dataset = None
    dataloader = DataLoader(dataset, batch_size=64, shuffle=False)

    predictions = []

    for inputs, labels in dataloader:
        output = model(inputs)

        predictions.extend(output.argmax(dim=1).tolist())
    
    accuracy = (predictions == labels).float().mean().item()
    print(f"Model{num} Accuracy: {accuracy:.2f}")


def ARC_test_3_times(models):
    for i in range(3):
        ARC_test(i, models[i])


