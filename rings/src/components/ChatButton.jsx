import PropTypes from 'prop-types';
import useStore from '../store';

export default function ChatButton({ id, name }) {
    const { setChatId } = useStore();

    const handleClick = () => {
        setChatId(id);
    }

    return (
        <button className="chatbutton" onClick={handleClick}>
            {name}
        </button>
    
    )
}

ChatButton.propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
}