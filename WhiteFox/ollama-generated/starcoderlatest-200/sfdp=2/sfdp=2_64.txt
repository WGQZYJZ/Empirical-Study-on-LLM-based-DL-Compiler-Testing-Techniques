
class AttentionModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, qk, key, value, scaled_qk, softmax_qk, dropout_qk, output):
        return output
    
    def _compute_scaled_qk(self, qk, key):
        return torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key

    def _compute_softmax_qk(self, scaled_qk):
        inv_scale_factor = math.sqrt(1 / qk.shape[-1])
        return scaled_qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor

    def _apply_dropout(self, softmax_qk):
        return torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.attention_module = AttentionModule()

    def forward(self, query, key, value, scaled_qk, softmax_qk, dropout_qk, output):
        return self.attention_module(query, key, value, scaled_qk, softmax_qk, dropout_qk, output)
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
