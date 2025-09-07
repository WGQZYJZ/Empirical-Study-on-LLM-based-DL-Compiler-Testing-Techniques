
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.relu(x1) 
        return v1
 
m  = Model() 
 
x1  = torch.randn(2,3,4,5)  # random input tensor (can be of any shape and size as long as it conforms to the model's expectations)

