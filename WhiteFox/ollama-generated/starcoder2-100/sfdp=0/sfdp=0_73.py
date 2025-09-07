

class MyModel(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.key = torch.nn.Linear(256 * 3*7*7, 1024)
        self.query = torch.nn.Linear(1024 * 8*8*8, 128)
        self.value = torch.nn.Linear(128 * 8*8*8, 64)

    def forward(self, inp): 
        v1  = self.key(inp)  # [1,3072]
        v2  = self.query(v1)  # [512,3,7,7]
        v3  = self.value(v1) #[64,8,8,8]
        v4 = torch.matmul(v2 / inv_scale, v3[:,:,:,:].transpose(-2,-1))
        return v4

