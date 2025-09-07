
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.concat  = torch.nn.Linear(48*128, 976)
 
    def forward(self, x1): 
        mat1 = torch.randn([x1.shape[1], 53]) # [batch_size X output]
        mat2 = torch.randn([int(mat1.shape[1]), int(mat1.shape[0]*48)]) # [input_length X batch size*output length]
        v1  = torch.addmm(x1, mat1, mat2) 
        v2  = self.concat(v1)
        return v2

# Initializing the model