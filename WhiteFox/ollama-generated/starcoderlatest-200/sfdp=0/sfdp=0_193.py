This pattern characterizes the Transformer model introduced by Vaswani et al., in which the Encoder is constructed as a series of layers, which consists of Multi-Head Self-Attention modules and a Layer Normalization module between them. The attention heads are constructed to have dimension `n_head = 8` while the value vector is usually set to `v = x`.


# Description of requirements
The model should contain the following pattern:
This pattern characterizes the EncoderBlock introduced by Vaswani et al., which consists of a series of Transformer modules, and it is used to compute output values from an input `x`. The Transformer module contains two Multi-Head Self-Attention layers with dimension `n_head = 8`, and the cross attention is performed between the first layer's self-attention output (`x1`) and the second layer's encoder output (`encoder_output`).


# Model
class FeedForward(torch.nn.Module):
    def __init__(self, hidden_dim: int = 512, ffn_dim: int = 2048):
        super().__init__()
        self.linear1 = torch.nn.Linear(ffn_dim, hidden_dim)
        self.activation = torch.nn.Tanh()

    def forward(self, x: torch.Tensor, attention_weights: torch.Tensor):
        ff_output = self.activation(self.linear1(attention_weights + self.dropout(x)))

        return ff_output
decoder_layer_input = tf.nn.LayerNormalization(x1 + self_attention_output) * tf.sqrt(1 / (self.n_head * head_dim))`

* 修 改


