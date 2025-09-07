
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # (N, C_in, H_q, W_q) * (C_out, N, K, 1) => (N, C_out, H_k, W_k)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # (N, C_in, H_k, W_k) * (C_out, N, K, 1) => (N, C_out, H_q, W_q)
        self.value = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # (N, C_in, H_v, W_v) * (C_out, N, K, 1) => (N, C_out, H_q, W_q)
        self.dropout = torch.nn.Dropout(0.25)
 
    def forward(self, x1): # query (N, C_in, H_q, W_q), key (N, C_in, H_k, W_k), value (N, C_in, H_v, W_v)
        qk = torch.matmul(self.query(x1), self.key(x1).transpose(-2, -1)) # (N, C_out, H_q, W_q) * (C_out, N, K, 1) => (N, C_out, H_k, W_k)
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = self.dropout(softmax_qk).matmul(self.value(x1)) # (N, C_out, H_q, W_q) * (C_out, N, K, 1) => (N, C_out, H_v, W_v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
