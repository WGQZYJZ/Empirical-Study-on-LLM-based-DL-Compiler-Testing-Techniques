
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:  # type: ignore[no-untyped-def]
        inv_scale_factor = math.sqrt(key.shape[-1])
 
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / inv_scale_factor  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)  # Apply dropout to the softmax output
 
        return dropout_qk.matmul(value)


# Initializing the model<|end_of_model|>
m  = Attention()
 

# Inputs to the model
query1  = torch.randn(3, 80, 768)
key1  = torch.randn(3, 256, 768)
value1  = torch.randn(3, 256, 129)
 
query2  = torch.randn(4, 100, 384)
key2  = torch.randn(4, 512, 384)
value2  = torch.randn(4, 512, 64)


__output_1__ = m(query1, key1, value1)
 
__output_2__ = m(query2, key2, value2)
 
# Initializing a new model. Notice the shape of inputs and outputs should match with that of previously generated model's. 
new_m  = Attention()

 # Inputs to the new model
query3  = torch.randn(10, 56, 768)
key3  = torch.randn(29, 400, 768)
value3  = torch.randn(4, 38, 128)

 # Outputs of the new model should be same as the outputs from previously generated model and new model.
output_3  = new_m(query3, key3, value3)