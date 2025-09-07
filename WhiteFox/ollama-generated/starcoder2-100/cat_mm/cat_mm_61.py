
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) # Matrix multiplication of two tensors.
        v2  = torch.cat([v1 for i in range(50)]) 
        return v2

# Initializing the model