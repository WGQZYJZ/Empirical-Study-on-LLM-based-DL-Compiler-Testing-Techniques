
class Model(torch.nn.Module):
    def __init__(self, input1_size=32, input2_size=64):
        super().__init__()
        
        self._input1 = torch.randn(input1_size)
        self._input2 = torch.randn(input2_size)
 
    def forward(self, *args): # Input tensor
        t1  = torch.mm(self._input1[None,...], self._input2[None,...])
        t3  = [t1 for i in range(5)] 
        t4  = [torch.cat([i for i in t3], dim=0) for j in t3] # Concatenate each matrix multiplication result along dimension 0, resulting in a 4D tensor
        
        return torch.sum(t4[0][None,...])

# Initializing the model and running forward pass
model = Model()
x1 = torch.randn(512)
x2 = torch.randn(768)
y = model([x1, x2])

