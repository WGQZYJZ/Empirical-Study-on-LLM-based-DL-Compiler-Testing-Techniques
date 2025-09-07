
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor1):
        v0 = torch.nn.functional.conv1d(input_tensor1) # Conv1d is invoked
        v2 = torch.nn.functional.batchnorm1d(v0, 3, 4, 5, 6) 
__output__  = m(x1)

