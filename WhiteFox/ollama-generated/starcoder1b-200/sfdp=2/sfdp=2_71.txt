
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scale = (torch.rand_like(v1) * max_scale).add_(min_scale).expand_as(v1)
        qk  = torch.matmul(v1, torch.transpose(v1, -2, -1)) / scale
        softmax_qk  = qk.softmax(-1)
        v2 = dropout(softmax_qk)
        output  = torch.matmul(v2, v1)
        return output


# Initializing the model
m  = Model()
