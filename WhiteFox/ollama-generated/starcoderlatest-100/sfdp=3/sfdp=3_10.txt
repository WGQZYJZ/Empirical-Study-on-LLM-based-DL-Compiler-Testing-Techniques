
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(self.query(x1), self.key(x2).transpose(-2, -1)) # compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # apply dropout to the softmax output
        output = dropout_qk.matmul(self.value) # compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
