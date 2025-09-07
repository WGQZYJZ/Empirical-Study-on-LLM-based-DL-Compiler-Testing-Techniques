
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Split(3, dim=1)
 
    def forward(self, x1):
        v1  = self.split(x1) # Splits the input tensor along dimension 0 using split_size_or_sections=[[256], [89]]
        v2  = torch.cat([v1[i] for i in range(len(self.split._splits))], dim=0) # Concatenates the tensors in the output of split along dimension 0 using a custom dim
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(3, 89 * 4 + 17, 56)
 
 