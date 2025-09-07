
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v0 = self.linear1(x1).permute(0, 2, 1) # Permute the first input tensor with 3 dimensions.
        return v0

# Initializing the model<|end_of_model|>
m  = Model()


