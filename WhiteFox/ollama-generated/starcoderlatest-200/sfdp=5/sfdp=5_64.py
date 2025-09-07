
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=768, n_head=12,
                 dropout_p=0., num_layers=4, dff=3072):
        super().__init__()
        self.multi_head_attention = MultiHeadAttention(
            embedding_dim=embedding_dim, num_heads=n_head, dropout_p=dropout_p)
        self.encoder_layer_norm = torch.nn.LayerNorm(embedding_dim)
        self.dense = torch.nn.Linear(embedding_dim, dff)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.layer_norm = torch.nn.LayerNorm(embedding_dim)
        self.pre_softmax = torch.nn.Linear(dff, embedding_dim)
 
        # Use multihead attention as the self-attention layer, and the query, key, value are set to be the input.
        # The original implementation of BERT is different from what is stated in the paper:
        # In that version, only the output (after adding multihead attention), or attn_layer (with linear layer)
        # will be used as the value for the self-attention layer, but in this case, it should be the input to
        # the self-attention layer. Therefore, in order to get the same results in both versions,
        # an extra step is added before the self-attention layer: (query @ key.transpose(-2,-1) / math.sqrt(query.size(-1))).view(batch_size, num_heads * embedding_dim).
        self.self_attention = MultiHeadAttention(
            embedding_dim=embedding_dim, num_heads=n_head, dropout_p=dropout_p)
 
    def forward(self, x):
        # x is the input to the model (in fact, there are different input types supported for transformer models)
        x = self.multi_head_attention(x, x, x)[0]
 
        output = self.encoder_layer_norm(x + self.dropout(torch.nn.functional.gelu(self.dense(x))))
 
        output = self.dropout(output)
        # This is the same as "pre-softmax", just that it's a linear layer instead of an activation function.
        x = self.layer_norm(output + torch.nn.functional.gelu(self.pre_softmax(output)))
 
        output, _  = self.self_attention((x, x, x), attn_mask=None)[0]
 
        return x
 
    def prepare_for_onnxruntime(self):
        # BERT requires that the model be exported as an onnx runtime module. In order to make sure all required operators
        # are supported by onnxruntime (like gelu and dropout with opset 12), this function is used to modify certain
        # layers in the exported model in a way that makes it compatible. In particular, dropout operations will be
        # replaced by equivalent ones from PyTorch (opset 10) or ONNXRuntime (opset 12) based on whether they're needed.
        # Please also add this function to your models if you want them to work with onnxruntime!
        self._convert_onnx_to_torch()
 
    def _convert_onnx_to_torch(self):
        for name, module in self.named_children():
            try:
                if 'layer_norm' in name or 'encoder_' in name:
                    # Dropout layers are handled differently in onnxruntime (and PyTorch) since some versions of pytorch use
                    # opset 10, and others use opset 12. In order to make sure the correct one is used by
                    # onnxruntime, we'll replace them with equivalent ones from PyTorch (opset 10), or ONNXRuntime
                    # (opset 12). See https://github.com/microsoft/onnxruntime for more details.
                    if module.__class__.__name__ == 'Dropout':
                        module = torch.nn.functional.dropout(
                            input=module, p=self.dropout.p, training=self.training)
                elif module.__class__.__name__ == 'LayerNorm':
                    # As layer normalization layers are not supported in onnxruntime, we will replace them with the pytorch
                    # equivalents instead to keep model compatibility between PyTorch and onnxruntime.
                    module = torch.nn.LayerNorm(module.normalized_shape, eps=module.eps)
                else:
                    self._convert_onnx_to_torch()
            except Exception as e:
                raise RuntimeError("Failed to convert '{}' to TorchScript format".format(name)) from e
 
# Initializing the model
m = Model()
m.prepare_for_onnxruntime()
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
