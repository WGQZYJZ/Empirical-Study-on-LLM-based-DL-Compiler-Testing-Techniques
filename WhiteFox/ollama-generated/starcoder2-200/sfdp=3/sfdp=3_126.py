
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1):
        v2 = torch.matmul(qk1[:, :, :64], qk1[:, :, 65:].transpose(-2, -1)) 
        v3 = self.scale_factor * v2  # Scale the dot product of the query and key tensors by a scale factor
        v4 = v3.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v5 = torch.nn.functional.dropout(v4, p=self.dropout_p)  # Apply dropout to the softmax output
        return v2 * self.dropout_qk[None].matmul(value)[0]


m = Model()
qk1 = torch.randn(8*8, 65, 67)
__output__  = m(qk1)