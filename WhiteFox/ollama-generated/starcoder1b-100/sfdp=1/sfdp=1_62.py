
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).mul_(0.7071067811865476).add_(1e-8) # scale by 0.7071067811865476, add epsilon to avoid divide by zero
        v3 = torch.nn.functional.dropout(v2, p=dropout_p) # apply dropout
        output = v3.matmul(value) # compute dot product of dropout output and value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
