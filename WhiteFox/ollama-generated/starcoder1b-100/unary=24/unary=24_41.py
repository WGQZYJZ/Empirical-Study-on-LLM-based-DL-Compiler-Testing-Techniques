
# Results and Discussion
We are using the input tensor as is, which has only three dimensions, but this model does not use it for any reason, so we do not see its use at all, which may indicate that the input data will be used in some cases in training. The model does not make any assumption about what kind of data we have, so it would be very surprising if it is able to handle the input data, but still we cannot say for sure for sure.

It may happen that the model has not yet been trained. In this case, it will have a relatively good result (overfitting), but you will not know whether your model is stable before it starts training. One way to mitigate such an issue would be to train the model until it reaches a point where it starts overfitting or gets some accuracy on the test set as a result of overfitting, and then use that model for inference.
