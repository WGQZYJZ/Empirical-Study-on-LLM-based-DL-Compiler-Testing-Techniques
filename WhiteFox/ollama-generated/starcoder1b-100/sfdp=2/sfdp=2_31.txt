
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = 0.7071067811865476  # Compute the inverse scale factor with which to scale the dot product of the query and key
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_qk = torch.matmul(v1, v1.transpose(-2, -1))
        softmax_qk  = scaled_qk / (self.scale_factor * self.scale_factor).sqrt_()
        output = softmax_qk.matmul(v1)
        return output


# Initializing the model
m = Model()


