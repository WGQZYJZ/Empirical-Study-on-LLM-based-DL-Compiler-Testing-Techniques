This pattern characterizes scenarios where the softmax of a query tensor and a key tensor is computed by adding them together, then the output of the dot product between these tensors and a scaled version of itself (which is applied elementwise) is returned.


# Model
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.transformer = torch.nn.Transformer(d_model=512, nhead=4, num_encoder_layers=3)
 
    def forward(self, x):
        output = self.transformer(x) # (batchsize, sequence_length, 1024)
        return output
