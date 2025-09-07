
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 256)
        self.fc2 = torch.nn.Linear(256, 4)
 
    def forward(self, x):
        v1 = x @ torch.transpose(x, 0, 1).contiguous() # Multiply x by transposed (transposed is equivalent to the transpose operation)
        v2 = self.fc1(v1) + 1  # Add 1 after multiplying x by the transpose
        v3 = self.fc2(v2) # Output of fc2 should be a vector, which means v3 should be an array
        return v3


# Initializing the model
m = Model()


