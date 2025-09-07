
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.randn(5, 3, 64, 64)
 
    def forward(self, x):
        v1  = self.conv(x) + self.other
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(3, 8, 64, 64)
 
 ## In your answer, please paste two code snippets:
 * The first one should be used as the inputs of the function `torch.nn.Conv2d` that is used in line `v1 = self.conv(x)`.
 * The second one should be used for initializing tensors in lines `self.other`.
