
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 8)
 
    def forward(self, qk):
        scaled_qk = qk / (1 / 64) # Apply the inverse scale factor to the dot product
        softmax_qk = scaled_qk.softmax(-1)
        output = self.matmul(softmax_qk)
        return output


# Inputs to the model
qk = torch.randn(1, 512, 8)
