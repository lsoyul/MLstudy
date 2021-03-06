import tensorflow as tf

# X and Y data
#x_train = [1,2,3]
#y_train = [1,2,3]

# Now we can use X and Y in place of x_data and y_data
# # Placeholders for a tensor that will be always fed using feed_dict
# See http://stackoverflow.com/questions/36693740/
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

# tf.Variable => trainable variable
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Our hypothesis xW+b
# hypopthesis = x_train * W + b
hypopthesis = X * W + b

# cost/Loss function
# cost = tf.reduce_mean(tf.square(hypopthesis - y_train))
cost = tf.reduce_mean(tf.square(hypopthesis - Y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initialize global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(5000):
    #sess.run(train)
    #if (step % 20) == 0:
    #    print(step, sess.run(cost), sess.run(W), sess.run(b))
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X:[1,2,3,4,5], Y:[2.1,3.1,4.1,5.1,6.1]})

    if(step % 20) == 0:
        print(step, cost_val, W_val, b_val)


