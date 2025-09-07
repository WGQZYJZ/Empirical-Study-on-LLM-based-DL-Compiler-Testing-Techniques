
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        vq = torch.matmul(x1, query)
        vq = vq / torch.sqrt(torch.diag(scale_factor))
        vs = value
        softmax = vs.softmax(-1)  # softmax on the values of the model
        dropout = vs * softmax  # apply dropout
        output = dropout * scale_factor  # dot product with the dropout result and the model's value tensor
