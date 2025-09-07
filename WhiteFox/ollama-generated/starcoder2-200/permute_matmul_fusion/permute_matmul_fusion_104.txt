
class Model(torch.nn.Module):
    def __init__(self, t1):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):

        v1  = x1.permute(0, 2, 1) # Permute the input tensor A
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        v3  = x1.permute(0, 2, 1).permute(0, 3, 2) # Permute the input tensor B
        v4  = torch.bmm(self.linear.weight, self.linear.weight) 

        v5  = torch.cat((v2, v3), dim=1) 
        return v5


# Initializing the model