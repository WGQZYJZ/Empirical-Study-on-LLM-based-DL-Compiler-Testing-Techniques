
class Model(torch.nn.Module):
    def __init__(self, n_head, dim_key=256, dim_value=384):
        super().__init__()
        self.dim_key = dim_key
        self.dim_value = dim_value
        self.head = torch.nn.Linear(in_features=n_head * dim_key, out_features=n_head * dim_key)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        k_scale_factor = self.dim_key ** (-0.5)  # Compute the inverse scale factor for the keys
        scaled_qk = qk / (k_scale_factor * torch.pow(k_scale_factor, -0.5))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

