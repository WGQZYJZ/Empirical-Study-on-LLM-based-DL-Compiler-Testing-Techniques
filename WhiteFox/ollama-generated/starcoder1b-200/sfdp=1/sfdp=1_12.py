
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        k1 = torch.randn(3, 8, 4, 4)
        scaled_k1 = k1.div(torch.norm(k1, dim=-1, keepdim=True).add(eps))
        scaled_v1 = v1.mul(scaled_k1)
        softmax_k1 = scaled_k1.softmax(-2)
        dropout_k1 = torch.nn.functional.dropout(softmax_k1, p=0.5)
        q1 = dropout_k1.matmul(v1)  # Compute the dot product of the dropout output and the value tensor
        return q1


# Initializing the model
m = Model()


