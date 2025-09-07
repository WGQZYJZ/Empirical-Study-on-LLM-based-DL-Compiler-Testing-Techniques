
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 3)
        self.linear2  = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = x1[..., [0]] # select the first feature channel from the input tensor
        v2 = torch.bmm(v1, self.linear1.weight.permute([1, 0])) + self.linear1.bias.view(-1, 3)

        v1 = x1[..., [1]] # select the second feature channel from the input tensor
        v2 += torch.matmul(v1, self.linear2.weight.permute([1, 0]).contiguous()) + self.linear2.bias.view(-1, 4)
        
        return v2

# Initializing the model
m = Model()

