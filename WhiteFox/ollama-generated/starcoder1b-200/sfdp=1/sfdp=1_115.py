
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 3, bias=False)
        self.dropout_p = 0.15
 
    def forward(self, x1, x2):
        qk = self.qkv(x1).transpose(-2, -1)  # Compute the dot product of the query and key tensors
        scale_factor = self.compute_scale_factor(qk)  # Scale the dot product by the inverse scale factor
        softmax_qk = qk / scale_factor  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        x3 = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return x3
 
    def compute_scale_factor(self, qk):
        q_sq = torch.einsum('bij,bki->bk', qk, qk)  # Compute the squared dot product of the query and key tensors
        div = (qk @ qk).sqrt() + 1e-12  # Add epsilon to avoid divide by zero
        return div / torch.sum(div, dim=-1, keepdim=True).expand_as(q_sq)


# Initializing the model
m = Model()


