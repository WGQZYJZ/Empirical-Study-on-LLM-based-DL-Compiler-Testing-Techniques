
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = torch.nn.Linear(768, 10)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x):
        v = self.dropout(torch.nn.functional.relu(
            self.layer_1(x)))  # ReLU activation for the input
        return v


# Initializing the model
m = Model()


