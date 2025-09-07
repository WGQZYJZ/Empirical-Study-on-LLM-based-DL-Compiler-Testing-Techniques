
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (x2 @ x2.transpose(-2, -1)) / 3
        v7 = dropout_p * ((x2.transpose(-2, -1).matmul(value).sum() / batch_size) / max_grad_norm) # Compute the gradient at the end of forward
        output  = dropout_qk * ((x1.transpose(-2, -1).matmul(v7).sum() / batch_size)) + \
                  v6 + output
 
    def reset_parameters(self):
        m.conv.reset_parameters_()


# Initializing the model
m = Model()

