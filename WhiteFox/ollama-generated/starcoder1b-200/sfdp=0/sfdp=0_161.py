
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 3 * 3, 10)
 
    def forward(self, x1):
        v1 = x1  # Unsqueeze to make the input a batch of size 1 x 1 x ... x 32 x ... x 32
        output  = self.linear(v1).view(-1, 10)  # Unsqueeze from the previous result
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
