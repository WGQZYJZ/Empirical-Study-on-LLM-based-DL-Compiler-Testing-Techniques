
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(d_model, d_k)
        self.linear_k = torch.nn.Linear(d_model, d_k)
        self.linear_v = torch.nn.Linear(d_model, d_k)
        self.dropout = torch.nn.Dropout(p=0.15)
        self.layer_norm1 = torch.nn.LayerNorm(d_k)
        self.layer_norm2 = torch.nn.LayerNorm(d_k)
 
    def forward(self, x):
        q = self.linear_q(x[:, 0])
        k = self.linear_k(x[:, 1])
        v = self.linear_v(x[:, 2])
 
        k = self.dropout(k)  # Use dropout to protect against the zero division
        scaled_qk = q @ k.transpose(-2, -1) / torch.exp(scaled_scale_factor * (k.norm(p=2, dim=-1) + v.norm(p=2, dim=-1)))  # Scale dot product by inverse scale factor and softmax
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)  # Apply dropout to the scaled dot product
        value = dropout_qk @ v  # Compute the dot product of the dropout output and the value
        return self.layer_norm1(value + x[:, 2])


# Initializing the model
m = Model()


