
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):

        v1 = torch.transpose(x1[:, :, :], 0, -2) # swap dim 1 and 3 of the tensor
        v2 = torch.matmul(v1, self.linear.weight) + self.linear.bias

        v3 = torch.bmm(torch.transpose(y1[:, :, :].permute(-1, -2), 0, -2).contiguous(), 
                        v2.view_as(torch.transpose(x1[:, :, :], 0, -2)).contiguous())
        return v3


# Initializing the model
m = Model()

