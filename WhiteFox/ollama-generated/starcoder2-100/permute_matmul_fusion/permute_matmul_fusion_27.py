class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 2, 1).contiguous() # Permute the input tensor A
        v2 = torch.bmm(v1, self.linear.weight)   # Permute the input tensor B

        v4 = v1.clone()                         # clone 1
        v5 = x1[:, :3].permute(0, 3, 2, 1).contiguous().clone() # clone 2
        v6 = torch.randn_like(v1)               # generate new tensor randomly
        
        v7 = v4 + x1                            # broadcasting
        v8 = v5 + self.linear                   # add 1
        v9 = v1 + self.linear                   # add 2
        v10 = x1[:, :3].clone()                 # clone 3

        return torch.bmm(v7, v6)                # call a bmm operator
