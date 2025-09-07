
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1, y1):
        v0 = torch.bmm(x1, y1) # or torch.matmul(x1,y1)
        v1 = x1[idx].permute(-1,-2).contiguous()
        v2 = v0 + self.linear(v1) 
        return v2

# Initializing the model
m  = Model()
__input_x1__, __input_y1__  = torch.randn(4,3), torch.randn(5,3,2)

# Inputs to the model
x1, y1  = torch.randn(10,2,786), torch.randn(50,3,2)
idx  = random_idx()

