import PropTypes from 'prop-types';

export default function Message({ role, content }) {


    return <div className={`message ${role == "assistant" ? "assistant" : "user"}`}>{role}: {content}</div>
}

Message.propTypes = {
    role: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
}