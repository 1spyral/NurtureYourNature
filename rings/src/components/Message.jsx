import PropTypes from 'prop-types';

export default function Message({ role, content }) {
    return (
        <div className={`message ${role === "assistant" ? "assistant" : "user"}`}>
            {role === "assistant" && (
                <div className="assistant-icon-container">
                    <img src="src/pictures/happy.png" alt="Assistant" className="assistant-icon" />
                </div>
            )}
            <div className="message-content">
                {role}: {content}
            </div>
        </div>
    );
}

Message.propTypes = {
    role: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
};
