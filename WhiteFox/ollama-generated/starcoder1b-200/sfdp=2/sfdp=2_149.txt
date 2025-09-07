
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.w_q = torch.nn.Linear(d_model, d_model)
        self.w_k = torch.nn.Linear(d_model, d_model)
        self.w_v = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.layer_norm1 = LayerNorm(d_model)
        self.layer_norm2 = LayerNorm(d_model)

    def forward(self, x):
        q = self.w_q(x).chunk(n=2, dim=-1)[0]  # Compute the left part of the query tensor
        k = self.w_k(x).chunk(n=2, dim=-1)[1]  # Compute the right part of the query tensor

        # Scale the dot product by an inverse scale factor
        # (query.key ** -0.5) * (input_mask.unsqueeze(-1))
        q_inv_scale = k.pow(-0.5).unsqueeze(-1) * input_mask  # A matrix containing zeros where element at row i, column j is set to one if the corresponding mask is non-zero
        dot_qk = q @ k.transpose(-2, -1)  # Compute the dot product of the query and key
        scaled_dot_qk = dot_qk / q_inv_scale  # Scale the dot product by an inverse scale factor
        softmax_dot_qk = F.softmax(scaled_dot_qk, dim=-1)  # Apply softmax to the scaled dot product

        dropout_dot_qk = self.dropout(softmax_dot_qk)  # Apply dropout to the softmax output

        v = self.w_v(x).chunk(n=2, dim=-1)[0]
        v = dropout_dot_qk.matmul(v)
        layer_norm1_out = self.layer_norm1(x + v)
        layer_norm2_out = self.layer_norm2(x + layer_norm1_out)

        return layer_norm2_out


# Initializing the model
m = Model(d_model)


