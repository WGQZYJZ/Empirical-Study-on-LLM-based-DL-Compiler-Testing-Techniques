
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, nhead * d_k)
        self.key = torch.nn.Linear(d_model, nhead * d_k)
        self.value = torch.nn.Linear(d_model, nhead * d_v)
        self.scale = torch.sqrt(torch.FloatTensor([d_k])).to('cuda')
 
    def forward(self, x1):
        q = self.query(x1)  # Compute the query tensor for each hidden state
        k = self.key(x1)  # Compute the key tensor for each hidden state
        v = self.value(x1)  # Compute the value tensor for each hidden state
        dk = torch.einsum('bm, bmb->bm', (k, v))  # Compute the dot product of the query and key tensors
        inv_dk = torch.rsqrt(torch.FloatTensor([nhead * d_k])).to('cuda') * dk
        scaled_qk = q @ k.transpose(-2, -1).div(inv_dk)  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk @ v  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

