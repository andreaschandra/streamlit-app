import streamlit as st

# streamlit stop()
# name = st.text_input('Name')
# if not name:
#     st.warning('Please input a name.')
#     st.stop()

# st.success('Thank you for inputing a name.')


def get_user_name():
    return 'John'


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
