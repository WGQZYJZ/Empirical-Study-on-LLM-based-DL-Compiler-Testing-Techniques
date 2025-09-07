
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.bmm(x1, x2)  # or torch.matmul(input_tensorA, input_tensorB)
        
        return v3

# Initializing the model
m = Model()

