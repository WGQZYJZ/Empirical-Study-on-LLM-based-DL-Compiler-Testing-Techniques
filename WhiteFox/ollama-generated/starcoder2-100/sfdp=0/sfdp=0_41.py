class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3):
        v0  = torch.matmul(input1, input2) / inv_scale 
        return v0 


m = Model()


v1 = np.random.rand(5184) * 0.9 + 0.1
v2 = np.random.rand(768) * 0.3 + 0.1
 
