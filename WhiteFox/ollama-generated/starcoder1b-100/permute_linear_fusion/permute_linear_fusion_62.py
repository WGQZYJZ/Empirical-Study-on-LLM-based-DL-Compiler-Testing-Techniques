The model can take multiple inputs for forward propagation, i.e., it should be defined as follows:

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, ... ): # This is a list of inputs to the model's forward propagation, and it should be defined as `v1, v2, ..., vn`.
