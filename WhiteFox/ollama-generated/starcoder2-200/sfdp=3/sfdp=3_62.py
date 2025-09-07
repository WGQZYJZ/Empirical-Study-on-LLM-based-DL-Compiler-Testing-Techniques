
class Model(torch.nn.Module):
    def __init__(self, scale_factor=0.5, dropout_p=0.2):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        # The original code contains a small mistake and it will be fixed in the public version of the model.
        # Original Code:
        #     scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor. The scale_factor here is missing a multiplication operation
        # Fixed Code:
        scaled_qk = query @ key.transpose(-2, -1).float().div(scale_factor) * scale_factor  # Compute the dot product of the query and key tensors. The scale_factor here is missing a multiplication operation.
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output.
        output  = dropout_qk @ value  # Compute the dot product of the dropout output and the value tensor.
        return output

# Initializing the model
scale_factor = 0.5
m1  = Model(scale_factor=scale_factor)


# Inputs to the model
key, query, value = torch.randn(32, 768), torch.randn(32, 768), torch.randn(32, 900)
__output1__, __output2__  = m1(query, key, value)


key, query, value = torch.randn(32, 768).float(), torch.randn(32, 768), torch.randn(32, 900)
__output1__, __output2__  = m1(query, key, value)


key, query, value = torch.randn(48, 50).float(), torch.randn(48, 768), torch.randn(32, 900)
__output1__, __output2__  = m1(query, key, value)

