class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.linear  = torch.nn.Linear(input1.shape[-1], 3)

    def forward(self, x1):
        v1_A = x1[0].permute(0, 2, 1) 
        v1_B = x1[1].permute(0, 2, 1)
        v2   = torch.bmm(v1_A, v1_B) 
        v3   = self.linear(v2)  
        return v3
