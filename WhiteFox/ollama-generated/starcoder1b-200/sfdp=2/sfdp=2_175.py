
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1, inv_scale_factor=1.0):
        super().__init__()
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor
 
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        scaled_qk = v1.matmul(v1.transpose(-2, -1)).div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
 
        v2 = dropout_qk.matmul(x1)
        return v2


# Initializing the model
m = Model()

