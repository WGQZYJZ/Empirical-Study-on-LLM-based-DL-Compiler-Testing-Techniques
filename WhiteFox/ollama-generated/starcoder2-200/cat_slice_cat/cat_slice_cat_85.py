
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inputs):

        # Concatenate all input tensors to a large, 2d matrix with shape (batch_size * 86, 1)
        t1 = torch.cat([inputs[0], inputs[3]], dim=1) 
        t2 = t1[:, :9223372036854775807]
        t3 = t2[:, :-size:]
        t4 = torch.cat(
            [
                # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
                t1, 
                t3 
            ], 
            dim=1)

        return t4


# Initializing the model
m = Model()
 
# Inputs to the model
input_tensor1 = torch.randn(batchSize, 256*3980, 17)
input_tensor2 = torch.randn(batchSize, 119*4975, 17)
input_tensors = [
    input_tensor1, 
    input_tensor2]
    
# Initial model forward pass.
output  = m(input_tensors)

