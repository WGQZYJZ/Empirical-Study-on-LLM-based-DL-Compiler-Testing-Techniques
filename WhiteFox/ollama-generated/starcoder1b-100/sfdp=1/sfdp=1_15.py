
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(self.feature_dim)
        scaled_qk = qk / math.sqrt(self.feature_dim)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(x1)
        return output


# Initializing the model
m = Model()

