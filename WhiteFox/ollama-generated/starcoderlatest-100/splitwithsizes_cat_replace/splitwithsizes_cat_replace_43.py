
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.classifier = torch.nn.Linear(64 * 7 * 7, num_classes)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=[48, 96, 144], dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1)
        return self.classifier(concatenated_tensor)
